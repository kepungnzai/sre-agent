

Install the dependencies

uv pip install .

uv add wikipedia

--------------------------------------------------------------------------------------------------
Run chrome in debug mode
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome-debug

This SRE agent comes with additional tool that is work in progress. It provide tool to call other llm tool via browser using OAuth. You must already login to the llm models. 

We have
- deepseek tool - pass and extract output from calling deepseek llm model
- browser tool- provide access to user browser to perform further searches and interact with external environment. In this case it is the observability tools. Agent will try to gather as much information as possible.
  

Browser tool interactions guide:- 

### 1. Load a page
browser_interact(action="load", page_url="https://example.com/login", tool_context=ctx)

### 2. Type into username field
browser_interact(action="type", input_selector="#username", text="myuser", tool_context=ctx)

### 3. Type password
browser_interact(action="type", input_selector="#password", text="pass123", tool_context=ctx)

### 4. Click login button
browser_interact(action="click", click_selector="#login-btn", tool_context=ctx)

### 5. Extract the resulting dashboard
result = browser_interact(action="extract", content_selector=".dashboard", tool_context=ctx)
print(result["response"])

### 6. Done – close the browser when finished
browser_interact(action="close", tool_context=ctx)


To run the main application for testing purposes, we need to ensure the agent is able to call these tools

Please ensure you have your .env inside workflow_agents folder. 

### To run the main program 
python main.py

<img width="1765" height="836" alt="image" src="https://github.com/user-attachments/assets/358b212b-97c5-40eb-aee3-13104aab0df5" />
