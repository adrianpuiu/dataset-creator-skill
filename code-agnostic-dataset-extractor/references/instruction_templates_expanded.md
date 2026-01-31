# Expanded Agent Instruction Templates: Code Patterns to Natural Language

**Author:** Manus AI

This document provides comprehensive mappings of common code patterns found in AI agent frameworks to their corresponding natural language instructions. This collection of 300+ entries demonstrates how users define complex agent logic, tool use, and reasoning entirely through text.

## Quick Reference by Category

| Category | Entries | Focus |
|----------|---------|-------|
| Core Agent Logic & Lifecycle | 50 | Initialization, execution, state management |
| Tool & Function Calling | 50 | Tool discovery, selection, execution, error handling |
| Data Processing & Manipulation | 50 | Transformation, cleaning, analysis, formatting |
| Communication & I/O | 50 | User interaction, logging, external channels |
| Advanced Reasoning & Planning | 50 | Planning, reflection, decision-making, logic |
| Specialized Skills & Domain Interaction | 50 | Databases, code, media, domain-specific tasks |

---

## 1. Core Agent Logic & Lifecycle (50 Entries)

Defines the agent's fundamental structure, initialization, and operational flow.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `class AgentCore:` | "Define the main brain of the agent" |
| `def __init__(self, config):` | "Set up the agent using its configuration settings" |
| `async def run(self, goal):` | "Start the agent's main process to achieve a goal" |
| `self.state = "running"` | "Set the agent's status to active" |
| `if self.is_paused:` | "Check if the agent should temporarily stop" |
| `self.max_iterations = 10` | "Limit the agent to a maximum of 10 steps" |
| `def save_state(self):` | "Remember the agent's current progress" |
| `def load_state(self):` | "Resume the agent from a previous save point" |
| `self.history.append(action)` | "Keep a record of every action the agent takes" |
| `def reset(self):` | "Clear all memory and start the agent fresh" |
| `self.config.model = "gpt-4.1-mini"` | "Specify the AI model the agent should use" |
| `def validate_input(self, user_input):` | "Check if the user's request is valid" |
| `if not user_input:` | "Handle cases where the user provides no input" |
| `self.log.info("Agent initialized")` | "Record that the agent has successfully started" |
| `def shutdown(self):` | "Gracefully stop the agent's operation" |
| `self.memory.clear()` | "Erase the agent's short-term memory" |
| `self.current_task_id += 1` | "Move to the next sub-task in the plan" |
| `def get_status(self):` | "Report the agent's current operational status" |
| `self.error_count = 0` | "Reset the counter for failed attempts" |
| `if self.is_critical_error:` | "Stop immediately if a major error occurs" |
| `def set_timeout(self, seconds):` | "Limit how long the agent can spend on a task" |
| `self.user_id = user.id` | "Identify the user who initiated the task" |
| `def update_config(self, new_settings):` | "Change the agent's settings during runtime" |
| `self.loop.run_until_complete(self.run())` | "Execute the agent until the task is finished" |
| `def handle_interrupt(self):` | "Respond to a user stopping the agent" |
| `self.context.update(new_data)` | "Add new information to the agent's working context" |
| `if self.context.is_stale:` | "Check if the information the agent has is outdated" |
| `def enforce_rules(self):` | "Make sure the agent follows all safety guidelines" |
| `self.max_retries = 3` | "Allow the agent to try a failed step up to 3 times" |
| `self.temperature = 0.2` | "Ensure the agent's responses are highly factual and less creative" |
| `def check_prerequisites(self):` | "Verify that all necessary conditions are met before starting" |
| `self.execution_time = time.time() - start_time` | "Calculate how long the task took to complete" |
| `def finalize_report(self):` | "Prepare the final document for the user" |
| `self.cost_estimate = calculate_tokens()` | "Estimate the computational cost of the task" |
| `if self.is_production_mode:` | "Use production-level resources and models" |
| `def log_performance(self):` | "Record metrics about the agent's efficiency" |
| `self.session_token = generate_token()` | "Create a unique identifier for the current session" |
| `def queue_task(self, task):` | "Put a new task in the waiting list" |
| `if self.queue.is_empty():` | "Check if there are no more tasks to process" |
| `def prioritize_task(self, task_id):` | "Move a specific task to the front of the queue" |
| `self.agent_name = "Manus"` | "Define the agent's name" |
| `def set_persona(self, persona_desc):` | "Adopt a specific character or communication style" |
| `self.system_prompt = load_file()` | "Load the agent's core instructions from a file" |
| `def switch_model(self, model_name):` | "Change the underlying AI model for a specific sub-task" |
| `if self.has_permission("admin"):` | "Check if the agent has administrative rights" |
| `def request_human_input(self):` | "Ask the user for clarification or a decision" |
| `self.feedback_loop.process(result)` | "Use the task outcome to improve future performance" |
| `def is_goal_achieved(self):` | "Determine if the main objective has been met" |
| `self.max_memory_size = "10MB"` | "Limit the size of the agent's working memory" |
| `def delegate_task(self, sub_agent):` | "Assign a part of the task to another specialized agent" |

---

## 2. Tool & Function Calling (50 Entries)

Governs how the agent discovers, selects, executes, and handles results of external tools.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `class WebScraperTool:` | "I need a tool that can download and read web pages" |
| `def __init__(self, tools):` | "I need to initialize my agent with some tools" |
| `async def execute_tool(name, args):` | "I want to run a specific tool and handle any errors" |
| `def register_tool(self, tool):` | "I want to add new tools to my agent" |
| `if tool_name in self.available_tools:` | "Check if the required tool is installed and ready" |
| `tool_result = await tool.run(args)` | "Execute the tool with the necessary inputs" |
| `if tool_result.is_error:` | "Handle the situation if the tool fails to run" |
| `def select_tool(self, task_description):` | "Choose the best tool for the current job" |
| `self.tool_schema = get_json_schema()` | "Provide the tool's technical documentation to the AI" |
| `if tool_name == "DatabaseQuery":` | "If the task involves data retrieval, use the database tool" |
| `def describe_tool_usage(self):` | "Explain to the user how the tool was used" |
| `self.tool_call_count += 1` | "Keep track of how many times tools are used" |
| `if self.tool_call_count > 5:` | "Stop using tools if the limit is reached" |
| `def validate_tool_args(self, args):` | "Ensure the inputs for the tool are correctly formatted" |
| `tool_output = parse_xml(raw_output)` | "Convert the tool's raw output into a usable format" |
| `def handle_tool_conflict(self, tool_a, tool_b):` | "Decide which tool to use when multiple options exist" |
| `self.tool_access_key = os.environ["API_KEY"]` | "Use the secret key to access the external tool" |
| `def log_tool_latency(self, latency):` | "Record how long the tool took to return a result" |
| `if tool.requires_confirmation:` | "Ask the user before executing a sensitive tool" |
| `def generate_tool_description(self, func):` | "Automatically create a natural language description for a new function" |
| `tool_name = self.context.get("next_tool")` | "Retrieve the name of the next tool from the plan" |
| `if tool_name.startswith("browser_"):` | "If the tool is a web action, use the browser interface" |
| `def retry_tool_call(self, tool_name, attempt):` | "Try running the tool again if it failed" |
| `self.tool_timeout = 60` | "Set a 60-second limit for tool execution" |
| `def map_nl_to_tool(self, nl_command):` | "Translate a user's request into a tool function call" |
| `if tool.is_deprecated:` | "Avoid using tools that are no longer supported" |
| `def check_tool_availability(self):` | "Verify that all necessary external services are online" |
| `tool_output_file = save_to_temp_file(output)` | "Save the tool's output to a temporary file" |
| `def release_tool_lock(self, tool_name):` | "Free up a tool so another agent can use it" |
| `if tool.is_rate_limited:` | "Pause execution if the tool's usage limit is hit" |
| `def get_tool_documentation(self, tool_name):` | "Retrieve the detailed instructions for a specific tool" |
| `tool_args = extract_args_from_prompt(prompt)` | "Identify the necessary inputs from the user's request" |
| `def prioritize_tool(self, tool_name):` | "Mark a specific tool as the preferred option" |
| `if tool.is_local:` | "Use the local version of the tool instead of the cloud service" |
| `def handle_api_rate_limit(self):` | "Implement a waiting period when an API limit is reached" |
| `tool_output_size = len(output)` | "Measure the amount of data returned by the tool" |
| `if tool_output_size > self.max_data_limit:` | "Stop processing if the tool returns too much data" |
| `def log_tool_parameters(self, params):` | "Record the exact inputs used for the tool call" |
| `self.tool_chain.append(tool_name)` | "Add the tool to the sequence of executed tools" |
| `def require_user_auth(self, tool_name):` | "Ensure the user is logged in before using this tool" |
| `if tool.is_expensive:` | "Warn the user before executing a high-cost tool" |
| `def create_new_tool(self, nl_spec):` | "Generate a new tool based on a natural language specification" |
| `tool_name = self.tool_registry.lookup("search")` | "Find the tool registered for web searching" |
| `def handle_tool_dependency(self, required_tool):` | "Ensure a prerequisite tool is run first" |
| `if tool.is_idempotent:` | "Check if running the tool multiple times is safe" |
| `def transform_tool_input(self, input_data):` | "Modify the input data to match the tool's required format" |
| `tool_output_schema = tool.get_output_schema()` | "Get the expected structure of the tool's result" |
| `def filter_tool_results(self, results):` | "Remove irrelevant information from the tool's output" |
| `if tool.is_async:` | "Run the tool in the background and continue processing" |
| `def report_tool_success(self, tool_name):` | "Confirm that the tool executed without issues" |

---

## 3. Data Processing & Manipulation (50 Entries)

Focuses on how the agent handles, transforms, and extracts insights from data.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `def format_output(results):` | "I want the agent's results formatted nicely" |
| `async def summarize(self, text):` | "I want to make long text shorter" |
| `data = json.loads(raw_text)` | "Convert the raw text into a structured data object" |
| `def extract_keywords(text):` | "Identify the most important words and phrases in the text" |
| `if data.is_empty():` | "Handle the case where the data source is blank" |
| `def clean_data(data_set):` | "Remove errors, duplicates, and inconsistencies from the data" |
| `data_set.filter(lambda x: x > 10)` | "Only keep data points that are greater than 10" |
| `def transform_to_csv(data):` | "Convert the data into a comma-separated file format" |
| `def calculate_average(numbers):` | "Find the mean value of this list of numbers" |
| `def group_by_category(data):` | "Organize the data based on their type or label" |
| `def visualize_data(data):` | "Create a chart or graph from the data" |
| `def sentiment_analysis(text):` | "Determine the emotional tone of the text" |
| `def translate_text(text, target_lang):` | "Convert the text into a different language" |
| `def redact_pii(document):` | "Remove all personal identifying information from the document" |
| `def check_data_integrity(data):` | "Verify that the data has not been corrupted or tampered with" |
| `def merge_dataframes(df1, df2):` | "Combine two different tables of data" |
| `def pivot_table(data, rows, cols):` | "Restructure the data to show relationships between fields" |
| `def generate_report_template(sections):` | "Create a standard layout for the final report" |
| `def count_occurrences(word, text):` | "Tally how many times a specific word appears" |
| `def normalize_text(text):` | "Convert all text to lowercase and remove punctuation" |
| `def split_document(document, max_size):` | "Break a large document into smaller, manageable chunks" |
| `def embed_text(text):` | "Convert the text into a numerical vector for comparison" |
| `def search_vector_db(query_vector):` | "Find similar information in the knowledge base" |
| `def deduplicate_list(items):` | "Remove all repeated entries from the list" |
| `def sort_by_date(records):` | "Arrange the records from newest to oldest" |
| `def calculate_percentage(part, whole):` | "Determine the ratio of one number to another" |
| `def format_currency(amount, currency):` | "Display the number as a monetary value" |
| `def parse_html_table(html_content):` | "Extract data from a table within a web page" |
| `def generate_synthetic_data(schema):` | "Create fake data that matches a given structure" |
| `def compress_file(file_path):` | "Reduce the size of the file for storage" |
| `def decompress_file(file_path):` | "Restore the file to its original size" |
| `def validate_email_format(email):` | "Check if the provided text is a valid email address" |
| `def calculate_median(numbers):` | "Find the middle value in the sorted list of numbers" |
| `def find_outliers(data, threshold):` | "Identify data points that are unusually far from the average" |
| `def apply_regex(pattern, text):` | "Use a regular expression to find specific text patterns" |
| `def convert_units(value, from_unit, to_unit):` | "Change a measurement from one unit to another" |
| `def create_index(document):` | "Build a searchable index for the document's content" |
| `def check_for_plagiarism(text):` | "Compare the text against a database to find copied content" |
| `def generate_caption(image_data):` | "Write a descriptive text for the image" |
| `def transcribe_audio(audio_file):` | "Convert the spoken words in the file to text" |
| `def extract_metadata(file_path):` | "Get information about the file, like creation date and author" |
| `def calculate_checksum(file_path):` | "Generate a unique code to verify the file's integrity" |
| `def anonymize_data(data_set):` | "Remove identifying characteristics from the data" |
| `def generate_summary_points(text, num_points):` | "Create a bulleted list of the main ideas" |
| `def categorize_document(document, categories):` | "Assign the document to one of the predefined topics" |
| `def resolve_entity_names(text):` | "Identify and link names of people, places, and organizations" |
| `def create_json_schema(data):` | "Define the structure of the data in a formal JSON format" |
| `def validate_against_schema(data, schema):` | "Check if the data conforms to the expected structure" |
| `def upscale_image(image_path):` | "Increase the resolution of the image" |
| `def detect_language(text):` | "Identify the language the text is written in" |

---

## 4. Communication & I/O (50 Entries)

Manages the agent's interaction with users, logging, and external communication.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `def send_email(recipient, subject, body):` | "Send a message to the user's email address" |
| `self.log.error("Task failed")` | "Record a critical failure in the agent's log" |
| `def post_to_slack(channel, message):` | "Share the result in the team's Slack channel" |
| `def receive_user_message(self):` | "Wait for a new message from the user" |
| `def format_for_mobile(text):` | "Make the text easy to read on a small phone screen" |
| `def generate_voice_response(text):` | "Convert the text into spoken audio" |
| `def read_from_clipboard(self):` | "Get the text that the user has copied" |
| `def write_to_clipboard(text):` | "Place the final result into the user's clipboard" |
| `def create_interactive_poll(question, options):` | "Ask the user a question with multiple choices" |
| `def send_notification(title, message):` | "Display a pop-up alert to the user" |
| `def set_response_tone(tone="professional"):` | "Ensure the agent's reply is professional" |
| `def check_user_preference(pref_key):` | "Look up the user's saved settings" |
| `def acknowledge_request(request_id):` | "Confirm to the user that the task has been received" |
| `def request_feedback(task_id):` | "Ask the user to rate the agent's performance" |
| `def handle_profanity(text):` | "Filter out inappropriate language from user input" |
| `def generate_follow_up_questions(topic):` | "Suggest next steps or related questions to the user" |
| `def present_as_table(data):` | "Display the data in a clear, structured table format" |
| `def present_as_markdown(text):` | "Format the output using Markdown syntax" |
| `def stream_response(chunk):` | "Send the result to the user piece by piece" |
| `def wait_for_confirmation(timeout):` | "Pause and wait for the user to click 'Yes' or 'No'" |
| `def send_sms(number, message):` | "Send a text message to the user's phone" |
| `def create_draft_reply(original_email):` | "Generate a response that the user can edit" |
| `def log_user_interaction(event):` | "Record every time the user talks to the agent" |
| `def set_verbosity_level(level="concise"):` | "Keep the agent's responses brief" |
| `def generate_error_message(error_code):` | "Create a user-friendly explanation for an error" |
| `def display_progress_bar(percentage):` | "Show the user how close the task is to completion" |
| `def attach_file(file_path):` | "Include a document or image with the final message" |
| `def check_for_new_files(directory):` | "Monitor a folder for recently added documents" |
| `def read_file_content(file_path):` | "Get the text content from a specified file" |
| `def write_file_content(file_path, content):` | "Save the generated text into a new file" |
| `def append_to_log(message):` | "Add a new line to the end of the log file" |
| `def create_directory(path):` | "Make a new folder in the file system" |
| `def delete_file(file_path):` | "Permanently remove a file from the system" |
| `def rename_file(old_name, new_name):` | "Change the name of a document" |
| `def list_directory_contents(path):` | "Show all files and folders in a location" |
| `def upload_to_cloud(file_path, service):` | "Move the file to a cloud storage service" |
| `def download_from_url(url):` | "Fetch a file from a link on the internet" |
| `def check_file_permissions(file_path):` | "Verify if the agent can read or write the file" |
| `def create_zip_archive(files):` | "Bundle multiple files into a compressed folder" |
| `def extract_zip_archive(zip_file):` | "Unpack the contents of a compressed folder" |
| `def set_file_encoding(encoding="UTF-8"):` | "Specify the character set for the file" |
| `def check_internet_connection(url):` | "Verify that the agent can access the internet" |
| `def ping_server(ip_address):` | "Test the connection speed to a remote machine" |
| `def open_browser_tab(url):` | "Launch a new window to visit a website" |
| `def close_browser_tab(tab_id):` | "Shut down a specific web page" |
| `def take_screenshot(url):` | "Capture an image of the web page" |
| `def scroll_webpage(direction):` | "Move down the web page to view more content" |
| `def click_element(element_id):` | "Simulate a mouse click on a button or link" |
| `def input_text_to_field(field_id, text):` | "Type text into a form field" |
| `def submit_form(form_id):` | "Send the completed form data" |

---

## 5. Advanced Reasoning & Planning (50 Entries)

Defines the agent's cognitive functions including planning, reflection, and decision-making.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `async def plan(self, goal):` | "I want my agent to break down big tasks into smaller steps" |
| `def reflect_on_failure(error_log):` | "Analyze why the previous step failed and learn from it" |
| `def self_correct(previous_action):` | "Adjust the plan based on the last action's unexpected result" |
| `def generate_hypotheses(data):` | "Formulate several possible explanations for the data" |
| `def evaluate_options(options, criteria):` | "Compare choices against rules to pick the best one" |
| `def maintain_long_term_memory(fact):` | "Store important information permanently" |
| `def retrieve_from_memory(query):` | "Search the agent's knowledge base for facts" |
| `def reason_by_analogy(problem):` | "Solve new problems by comparing to similar past cases" |
| `def identify_dependencies(task_list):` | "Determine which tasks must be completed before others" |
| `def create_decision_tree(choices):` | "Map out the possible outcomes for each choice" |
| `def check_for_logical_fallacies(argument):` | "Verify that reasoning is sound and error-free" |
| `def prioritize_subtasks(tasks, urgency):` | "Order steps based on how quickly they need completion" |
| `def determine_next_step(current_state):` | "Figure out the single most logical action to take" |
| `def ask_for_clarification(ambiguous_term):` | "Request a more precise definition" |
| `def simulate_outcome(action):` | "Predict what will happen if the agent takes this action" |
| `def detect_contradiction(statements):` | "Find conflicting information in the data" |
| `def update_plan(new_information):` | "Modify the existing plan to account for new facts" |
| `def generate_alternative_plan(failed_plan):` | "Create a completely different strategy" |
| `def set_confidence_score(result):` | "Rate how certain the agent is about the result" |
| `if self.confidence_score < 0.8:` | "Flag uncertain results for human review" |
| `def perform_sanity_check(result):` | "Check if the final answer makes common sense" |
| `def identify_root_cause(symptoms):` | "Determine the underlying reason for the problem" |
| `def generate_pro_con_list(topic):` | "Create a balanced list of advantages and disadvantages" |
| `def synthesize_multiple_sources(sources):` | "Combine information from several documents" |
| `def abstract_concept(details):` | "Explain complex details using simple concepts" |
| `def concretize_concept(abstract_idea):` | "Provide specific, real-world examples" |
| `def maintain_working_memory(data):` | "Keep data readily available for immediate use" |
| `def compress_memory(old_data):` | "Summarize and archive old information" |
| `def perform_critical_review(document):` | "Analyze the document for biases and weaknesses" |
| `def generate_test_cases(function_spec):` | "Create examples to verify function correctness" |
| `def perform_backtracking(last_step):` | "Undo the last action and try a different path" |
| `def set_risk_tolerance(level="low"):` | "Ensure the agent takes only minimal-risk actions" |
| `def perform_ethical_check(action):` | "Verify the action aligns with ethical guidelines" |
| `def identify_missing_information(plan):` | "List all the facts the agent still needs" |
| `def generate_outline(topic):` | "Create a structured table of contents" |
| `def enforce_style_guide(text, style):` | "Make sure the writing matches the required format" |
| `def create_milestone(description, deadline):` | "Set a major checkpoint for the task" |
| `def check_milestone_status(milestone_id):` | "Report whether the checkpoint has been reached" |
| `def generate_visual_plan(plan_steps):` | "Create a flowchart of the execution plan" |
| `def perform_recursive_search(query):` | "Search iteratively for deeper information" |
| `def identify_causal_link(events):` | "Determine cause-and-effect relationships" |
| `def perform_deductive_reasoning(premises):` | "Use general rules to reach specific conclusions" |
| `def perform_inductive_reasoning(observations):` | "Use observations to form general rules" |
| `def generate_counter_argument(thesis):` | "Create a strong argument opposing the main point" |
| `def assess_novelty(result):` | "Determine if the result is new or already known" |
| `def set_priority_queue(tasks):` | "Organize sub-tasks by importance and urgency" |
| `def check_for_bias(data_set):` | "Analyze the data for unfair representation" |
| `def generate_summary_of_changes(old, new):` | "List differences between two documents" |
| `def perform_peer_review(document):` | "Critique as if reviewed by an expert" |
| `def determine_feasibility(plan, resources):` | "Assess if the plan can be executed realistically" |

---

## 6. Specialized Skills & Domain Interaction (50 Entries)

Relates to domain-level capabilities including databases, code, and media.

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `class SkillDatabase:` | "I need a skill that can work with databases" |
| `def execute_sql_query(query):` | "Run this SQL command against the database" |
| `def connect_to_db(credentials):` | "Establish a connection to the database server" |
| `def insert_record(table, data):` | "Add a new row of data to the specified table" |
| `def update_record(table, condition, new_data):` | "Change the information in an existing database entry" |
| `def delete_record(table, condition):` | "Remove a row from the database that meets a condition" |
| `def check_table_schema(table_name):` | "Get the structure and column names of the table" |
| `def begin_transaction():` | "Start a sequence of database operations that must all succeed" |
| `def commit_transaction():` | "Save all changes made in the current sequence" |
| `def rollback_transaction():` | "Cancel all changes made since the start of the sequence" |
| `def run_python_code(code_block):` | "Execute this block of Python programming code" |
| `def debug_code(code_block):` | "Find and fix any errors in the provided code" |
| `def generate_unit_test(function_name):` | "Write a test to verify the function's correctness" |
| `def refactor_code(code_block):` | "Improve the structure and readability of the code" |
| `def translate_code(source_lang, target_lang, code):` | "Convert the code from one language to another" |
| `def check_code_security(code_block):` | "Scan the code for security vulnerabilities" |
| `def install_package(package_name):` | "Add this new software library to the environment" |
| `def run_shell_command(command):` | "Execute this command in the terminal" |
| `def check_os_version():` | "Determine the operating system the agent is on" |
| `def manage_docker_container(action, container_id):` | "Start, stop, or restart the Docker container" |
| `def generate_image(prompt):` | "Create a new image based on this text description" |
| `def edit_image(image_path, instructions):` | "Modify the existing image according to instructions" |
| `def generate_video(prompt, duration):` | "Create a short video clip based on the description" |
| `def generate_audio(prompt, style):` | "Create a sound clip or music track" |
| `def convert_image_format(input_path, output_format):` | "Change the image file type" |
| `def apply_image_filter(image_path, filter_name):` | "Add a visual effect to the image" |
| `def crop_image(image_path, dimensions):` | "Cut the image to a specific size" |
| `def resize_image(image_path, width, height):` | "Change the image's dimensions" |
| `def generate_slides(content_file):` | "Create a presentation deck from content" |
| `def export_slides(slides_uri, format):` | "Save the presentation as a PDF or PowerPoint" |
| `def add_slide_notes(slide_id, notes):` | "Include speaker notes for a specific slide" |
| `def create_chart(data, chart_type):` | "Generate a bar chart or pie chart from data" |
| `def update_spreadsheet_cell(file, sheet, cell, value):` | "Change a specific value in the spreadsheet" |
| `def calculate_spreadsheet_formula(file, sheet, formula):` | "Run a calculation within the spreadsheet" |
| `def create_new_sheet(file, sheet_name):` | "Add a new tab to the spreadsheet document" |
| `def generate_pdf_from_html(html_content):` | "Convert web page code into a PDF document" |
| `def sign_document(document_path, signature):` | "Apply a digital signature to the file" |
| `def encrypt_file(file_path, password):` | "Protect the file with a password" |
| `def decrypt_file(file_path, password):` | "Remove the password protection from the file" |
| `def check_blockchain_status(network):` | "Verify the current state of the cryptocurrency network" |
| `def retrieve_stock_price(ticker):` | "Get the current market value for this company's stock" |
| `def check_weather(city):` | "Find the current weather conditions for a location" |
| `def get_current_time(timezone):` | "Report the exact time in a specific region" |
| `def set_calendar_event(title, start_time, end_time):` | "Add a new meeting or appointment to the calendar" |
| `def check_inventory(product_id):` | "Look up the current stock level for a product" |
| `def process_payment(amount, method):` | "Handle a financial transaction" |
| `def book_flight(origin, destination, date):` | "Search for and reserve a flight" |
| `def generate_legal_disclaimer(topic):` | "Create a standard legal warning for the subject" |
| `def perform_medical_diagnosis(symptoms):` | "Analyze symptoms to suggest a possible condition" |
| `def create_3d_model(prompt):` | "Generate a three-dimensional object from description" |

---

## 7. Additional Entries (10 Entries)

| Code Pattern | Natural Language Instruction |
| :--- | :--- |
| `def check_for_dead_links(url_list):` | "Verify that all links in the list are still working" |
| `def generate_qr_code(data):` | "Create a scannable image for this data" |
| `def perform_a_b_test(variant_a, variant_b):` | "Compare the performance of two different versions" |
| `def set_cookie(key, value, expiry):` | "Store a small piece of data in the browser" |
| `def clear_cache():` | "Delete all temporary files to speed up the system" |
| `def check_for_updates(software_name):` | "See if a newer version of the software is available" |
| `def create_user_account(username, password):` | "Register a new user in the system" |
| `def delete_user_account(user_id):` | "Permanently remove a user's profile" |
| `def generate_password(length, complexity):` | "Create a strong, random security code" |
| `def perform_network_scan(ip_range):` | "Check all devices connected to the local network" |

---

## How to Use This Reference

### For Dataset Extraction

When analyzing code, recognize patterns from this guide and map them to natural language:

1. **Identify the pattern** — Look for code matching the "Code Pattern" column
2. **Translate naturally** — Use the "Natural Language Instruction" as a guide
3. **Customize** — Adapt the instruction to fit the specific implementation
4. **Generate messages** — Create the conversational format entry

### Example

**Code Found:**
```python
def execute_tool(name, args):
    tool = self.tools[name]
    result = await tool.run(args)
    return result
```

**Pattern Matched:** `async def execute_tool(name, args):`

**Template Suggestion:** "I want to run a specific tool and handle any errors"

**Generated Instruction:** "I want to execute a specific tool with parameters and capture the result"

**Full Entry:**
```json
{
  "messages": [
    {"role": "system", "content": "You are an expert programmer..."},
    {"role": "user", "content": "I want to execute a specific tool with parameters and capture the result"},
    {"role": "assistant", "content": "```python\nasync def execute_tool(name, args):\n    tool = self.tools[name]\n    result = await tool.run(args)\n    return result\n```"}
  ]
}
```

---

## Notes

- Patterns are organized by functional category
- Natural language instructions should be non-technical and user-focused
- Feel free to adapt templates to match specific implementations
- This is a living reference — new patterns should be added as they're discovered
- The goal is consistency and clarity in translating code to natural language
