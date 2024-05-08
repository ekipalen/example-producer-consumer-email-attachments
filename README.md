# Example: Read email attachments from the email that triggers CR process

## Tasks

The robot is split into two tasks, meant to run as separate steps in Control Room. The first task generates (produces) data by reading the attachments from the email that triggers the process, and the second one reads (consumes) and processes that data.

### The first task (the producer)

- Load the example Excel file from work item created from the email that triggers the process
- Split the Excel file into work items for the consumer

### The second task (the consumer)

- Loop through all work items in the queue and access the payloads from the previous step

Start writing Python and remember that the AI/LLM's out there are getting really good and creating Python code specifically.

👉 Try out [Robocorp ReMark 💬](https://chat.robocorp.com)

For more information, do not forget to check out the following:
- [Robocorp Documentation -site](https://robocorp.com/docs)
- [Portal for more examples](https://robocorp.com/portal)
- Follow our main [robocorp -repository](https://github.com/robocorp/robocorp) as it is the main location where we developed the libraries and the framework.