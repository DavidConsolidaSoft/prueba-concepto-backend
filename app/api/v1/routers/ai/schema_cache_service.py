import os
import json
import time
import logging
from typing import List, Dict, Any, Optional, Set
from app.api.v1.routers.ai.redis_service import RedisService

logger = logging.getLogger(__name__)

class SchemaCache:
    """
    Service for caching and managing schema metadata.
    Provides efficient access to schema information that's already stored in Redis.
    """
    def __init__(self):
        # Initialize services
        self.redis_service = RedisService()
        
        # Redis key prefixes
        self.TABLE_KEY_PREFIX = "schema:table:"
        self.EMBEDDING_KEY_PREFIX = "schema:embedding:"
        self.ALL_TABLES_KEY = "schema:all_tables"
        
    def get_all_tables(self) -> List[str]:
        """
        Get a list of all available tables in the schema.
        
        Returns:
            List of table names
        """
        try:
            tables = self.redis_service.redis_client.smembers(self.ALL_TABLES_KEY)
            return list(tables) if tables else []
        except Exception as e:
            logger.error(f"Error getting all tables: {str(e)}")
            return []
    
    def get_table_metadata(self, table_name: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata for a specific table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            Dictionary with table metadata or None if not found
        """
        try:
            table_key = f"{self.TABLE_KEY_PREFIX}{table_name}"
            table_data = self.redis_service.redis_client.get(table_key)
            
            if table_data:
                return json.loads(table_data)
            
            return None
        except Exception as e:
            logger.error(f"Error getting table metadata for {table_name}: {str(e)}")
            return None
    
    def get_multiple_tables_metadata(self, table_names: List[str]) -> Dict[str, Dict]:
        """
        Get metadata for multiple tables in one operation.
        
        Args:
            table_names: List of table names
            
        Returns:
            Dictionary mapping table names to their metadata
        """
        result = {}
        
        try:
            # Use Redis pipeline for efficiency
            pipeline = self.redis_service.redis_client.pipeline()
            
            # Queue all get operations
            for table_name in table_names:
                table_key = f"{self.TABLE_KEY_PREFIX}{table_name}"
                pipeline.get(table_key)
            
            # Execute pipeline
            responses = pipeline.execute()
            
            # Process responses
            for i, table_name in enumerate(table_names):
                if responses[i]:
                    try:
                        result[table_name] = json.loads(responses[i])
                    except json.JSONDecodeError:
                        logger.warning(f"Invalid JSON for table {table_name}")
            
            return result
        except Exception as e:
            logger.error(f"Error getting multiple tables metadata: {str(e)}")
            return result
    
    def get_columns_for_table(self, table_name: str) -> List[Dict[str, Any]]:
        """
        Get column information for a specific table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            List of columns with their metadata
        """
        table_metadata = self.get_table_metadata(table_name)
        
        if table_metadata and 'columnas' in table_metadata:
            return table_metadata['columnas']
        
        return []
    
    def get_primary_key_for_table(self, table_name: str) -> Optional[str]:
        """
        Get the primary key column name for a table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            Name of the primary key column or None
        """
        columns = self.get_columns_for_table(table_name)
        
        for column in columns:
            if column.get('is_key', False):
                return column['name']
        
        return None
    
    def get_relations_for_table(self, table_name: str) -> List[Dict[str, Any]]:
        """
        Get relations for a specific table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            List of relations
        """
        table_metadata = self.get_table_metadata(table_name)
        
        if table_metadata and 'relaciones' in table_metadata:
            return table_metadata['relaciones']
        
        return []
    
    def get_schema_summary(self, include_columns: bool = False) -> Dict[str, Any]:
        """
        Get a summary of the entire schema.
        
        Args:
            include_columns: Whether to include column details
            
        Returns:
            Schema summary
        """
        try:
            tables = self.get_all_tables()
            
            summary = {
                "total_tables": len(tables),
                "tables": {}
            }
            
            if include_columns:
                # Get detailed information
                for table_name in tables:
                    metadata = self.get_table_metadata(table_name)
                    if metadata:
                        summary["tables"][table_name] = metadata
            else:
                # Just include table names
                summary["tables"] = {table: {} for table in tables}
            
            return summary
        except Exception as e:
            logger.error(f"Error getting schema summary: {str(e)}")
            return {"total_tables": 0, "tables": {}}
    
    def search_tables_by_name(self, search_term: str) -> List[str]:
        """
        Search for tables by name.
        
        Args:
            search_term: Search term to match against table names
            
        Returns:
            List of matching table names
        """
        all_tables = self.get_all_tables()
        search_term_lower = search_term.lower()
        
        # Find tables that contain the search term
        matching_tables = [
            table for table in all_tables 
            if search_term_lower in table.lower()
        ]
        
        return matching_tables
    
    def search_tables_by_column(self, column_name: str) -> List[str]:
        """
        Find tables that have a specific column.
        
        Args:
            column_name: Name of the column to search for
            
        Returns:
            List of table names that have this column
        """
        all_tables = self.get_all_tables()
        column_name_lower = column_name.lower()
        matching_tables = []
        
        for table_name in all_tables:
            columns = self.get_columns_for_table(table_name)
            
            # Check if any column matches
            if any(col['name'].lower() == column_name_lower for col in columns):
                matching_tables.append(table_name)
        
        return matching_tables