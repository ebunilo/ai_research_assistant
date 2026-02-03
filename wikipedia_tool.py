import wikipedia

def wikipedia_tool(query: str) -> str:
    """
    Searches Wikipedia for a given query and returns a summary of the top result.

    Args:
        query (str): The search term to look up on Wikipedia.
    """
    try:
        # The summary method automatically finds the best-matching page
        # and returns a summary of it.
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle cases where a query is ambiguous (e.g., "Java")
        return f"The query '{query}' is ambiguous. Please be more specific. Options: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        # Handle cases where the page does not exist
        return f"Sorry, I could not find a Wikipedia page for '{query}'."
    except Exception as e:
        return f"An unexpected error occurred while searching Wikipedia: {e}"
