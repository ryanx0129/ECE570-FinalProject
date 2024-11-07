import logging

# Initialize logging for result aggregation
logging.basicConfig(level=logging.DEBUG, filename='result_aggregation.log', format='%(asctime)s - %(levelname)s - %(message)s')

def aggregate_results(results):
    """Aggregates results from each prompt and classification."""
    logging.debug("Aggregating results")
    summary = {"GOOD BOT": 0, "BAD BOT": 0, "Repeating Prompt": 0, "Irrelevant": 0, "UNCLEAR": 0}
    for _, _, classification in results:
        summary[classification] += 1
    logging.debug(f"Aggregated summary: {summary}")
    return summary

def summarize_results(results):
    """Prints a summary of classification results."""
    summary = aggregate_results(results)
    print("Results Summary:")
    for category, count in summary.items():
        print(f"{category}: {count}")
    logging.info("Summary printed successfully")
