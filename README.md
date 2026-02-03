# AI Research Assistant

This solution builds an intelligent, automated **Research Assistant** that will replace the entire manual research workflow with a single, seamless interaction. Instead of performing a dozen manual steps, the user will simply provide a single directive to the agent, such as: **Research the topic of CRISPR gene editing.**

From that point on, the agent will take over, orchestrating a complete research process autonomously. The agent’s automated plan will be designed to intelligently mimic the steps of a human researcher, but with the speed and efficiency of a machine. It will be responsible for:

- Automatically querying Wikipedia to retrieve a high-level summary.

- Automatically searching the arXiv database to find relevant and recent academic papers.

- Automatically performing a general web search to gather supplementary, real-time context on the topic.
- Automatically synthesizing all the collected information into a single, structured report file.

By automating this sequence, the agent will solve the core problem of inefficiency and context switching, delivering a comprehensive research output in a fraction of the time it would take a human to do so manually.

## The Agent's Brain

The core of our agent’s intelligence and planning ability will come from its instruction parameter. For a complex, multi-step task like this, the instruction prompt is not just a simple directive; it is the agent’s master plan. We will craft a detailed, comprehensive prompt that explicitly tells the LLM the exact sequence of steps it must follow to complete the research workflow successfully.

This prompt will instruct the agent to:

- Begin by researching the topic. It should use the `wikipedia_tool` for general information, the `arxiv_tool` for academic papers, and the `GoogleSearchTool` tool for supplementary web-based context.

- Synthesize the findings. After gathering information from all three sources, it must synthesize the content into a single, coherent report.

- Save the result. Finally, it must use the `report_writer_tool` to save the complete report to a file.

By encoding the entire workflow into the instruction prompt, we are using the LLM’s powerful reasoning and sequencing capabilities to drive the agent’s behavior from start to finish.

## The Agent's Tools

To equip our Research Assistant with the necessary capabilities, we will provide it with a set of specialized tools:

- `wikipedia_tool`: It is a custom Python function we will write that takes a search query as input. It will use a third-party Python library to interact with the Wikipedia library and return a concise summary of the relevant article.

- `arxiv_tool`: It is a custom Python function that will take a search query. It will use a Python wrapper for the public arXiv API to find the most recent and relevant academic papers, returning their titles and summaries.

- `GoogleSearchTool`: It is the built-in tool to find supplementary, real-time information from across the web. We will use this powerful, prebuilt tool provided by the ADK framework. This tool enables the agent to perform a Google search and receive a summary of the results.

- `report_writer_tool`: It is a simple utility function that will take a string of text (the agent’s research notes) and a file name as input. Its job is to write this content to a local file, simulating the creation of the final report.

## Features

- **Single Command Research**: Initiate a complete research workflow with a single directive.
- **Multi-Source Data Gathering**: Collect information from Wikipedia, arXiv, and general web searches.
- **Automated Synthesis**: Compile and structure the gathered data into a coherent report.
- **Time Efficiency**: Drastically reduce the time required for research tasks.
- **Contextual Understanding**: Mimic human research strategies for effective information retrieval.
- **Customizable Output**: Generate reports in various formats (e.g., PDF, Word, Markdown).
- **Scalability**: Handle multiple research topics simultaneously.