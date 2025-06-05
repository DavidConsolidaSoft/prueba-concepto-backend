import requests
import json
import time

# Base URL for API
BASE_URL = "http://localhost:8000"

def test_dynamic_query(query_text):
    """
    Test the dynamic query API endpoint.
    
    Args:
        query_text: Natural language query text
    """
    url = f"{BASE_URL}/api/v1/reportes/dynamic-query"
    
    # Prepare request payload
    payload = {
        "text": query_text,
        "limit": 20,  # Limit results to 20
        "pagination": False  # Don't use pagination for this test
    }
    
    # Make the request
    print(f"Sending query: {query_text}")
    start_time = time.time()
    
    try:
        response = requests.post(url, json=payload)
        
        # Print timing
        elapsed = time.time() - start_time
        print(f"Response received in {elapsed:.2f} seconds")
        
        # Check response
        if response.status_code == 200:
            data = response.json()
            
            # Print results summary
            print(f"Query successful - {len(data['results'])} results out of {data['total_results']}")
            print(f"Processing time (server): {data['processing_time']:.2f} seconds\n")
            
            # Print ORM code generated
            print("Generated ORM code:")
            print("-" * 50)
            print(data['orm_code'])
            print("-" * 50)
            
            # Print sample results
            if data['results']:
                print("\nSample results:")
                for i, result in enumerate(data['results'][:3]):
                    print(f"  Result {i+1}: {result}")
                
                if len(data['results']) > 3:
                    print(f"  ... and {len(data['results']) - 3} more results")
            
            return data
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Test queries
    test_queries = [
        "Obtener las 10 cajas más recientes",
        "¿Cuántos clientes activos tenemos?",
        "Dame el top 5 de productos más vendidos",
        "Lista todas las facturas del mes pasado",
        "Muestra los bancos con preferido=1",
        "¿Cuál es el total de ventas por día en la última semana?"
    ]
    
    # Run each test query
    for query in test_queries:
        print("\n" + "="*60)
        result = test_dynamic_query(query)
        print("="*60 + "\n")
        
        # Pause between requests to avoid rate limiting
        time.sleep(2)