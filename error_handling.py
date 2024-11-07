import logging

# Initialize logging for error handling
logging.basicConfig(level=logging.DEBUG, filename='error_handling.log', format='%(asctime)s - %(levelname)s - %(message)s')

class ModelError(Exception):
    """Custom exception for model-related errors."""
    pass

def safe_query_model(model_func, *args, **kwargs):
    """Wrapper function that safely queries the model and handles exceptions."""
    try:
        logging.info("Querying model safely")
        return model_func(*args, **kwargs)
    except ModelError as e:
        logging.error(f"ModelError occurred: {e}")
        return "ModelError: Unable to process the query"
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "An unexpected error occurred"

if __name__ == "__main__":
    def mock_model_query(prompt):
        if "error" in prompt:
            raise ModelError("Simulated model error")
        return f"Mock response for: {prompt}"

    response = safe_query_model(mock_model_query, "Test prompt with no error")
    print(response)
    response_with_error = safe_query_model(mock_model_query, "Test prompt with error")
    print(response_with_error)
