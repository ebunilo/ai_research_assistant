import arxiv

def arxiv_tool(query: str) -> str:
    """
    Searches the arXiv repository for academic papers matching a query.

    Args:
        query (str): The topic to search for academic papers on.
    """
    try:
        # Create a client to interact with the arXiv API
        client = arxiv.Client()

        # Define the search parameters
        search = arxiv.Search(
            query=query,
            max_results=2,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        results = []
        # Use the client to execute the search and get the results
        for result in client.results(search):
            results.append(f"Title: {result.title}\nSummary: {result.summary}\nURL: {result.entry_id}")
            
        if not results:
            return f"No academic papers found on arXiv for the query '{query}'."
            
        return "\n---\n".join(results)
        
    except Exception as e:
        return f"An unexpected error occurred while searching arXiv: {e}"
    