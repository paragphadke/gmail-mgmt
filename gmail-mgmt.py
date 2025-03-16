import mailbox
import os
import email
from collections import defaultdict
import pandas as pd
import ace_tools as tools  # For displaying the dataframe

# Path to the extracted .mbox file from Google Takeout
MBOX_FILE_PATH = "All mail including Spam and Trash.mbox"

# Function to process the .mbox file
def process_mbox(mbox_file):
    label_counts = defaultdict(int)  # Store email count per label
    label_sizes = defaultdict(int)   # Store total size per label (bytes)

    # Open the .mbox file
    mbox = mailbox.mbox(mbox_file)

    for message in mbox:
        if message is None or not isinstance(message, mailbox.mboxMessage):
            continue
        
        # Extract the labels from Gmail's specific header
        labels = message.get("X-Gmail-Labels", "").split(",")
        
        # Get the size of the email
        email_size = len(str(message))  # Approximate size in bytes

        for label in labels:
            label = label.strip()
            if label:
                label_counts[label] += 1
                label_sizes[label] += email_size

    # Convert results to a DataFrame for better visualization
    report_df = pd.DataFrame({
        "Label": label_counts.keys(),
        "Number of Emails": label_counts.values(),
        "Total Size (MB)": [round(size / (1024 * 1024), 2) for size in label_sizes.values()],  # Convert bytes to MB
        "Total Size (GB)": [round(size / (1024 * 1024 * 1024), 2) for size in label_sizes.values()]  # Convert bytes to GB
    })

    return report_df

# Run the script and generate report
email_report = process_mbox(MBOX_FILE_PATH)

# Display the report
tools.display_dataframe_to_user(name="Gmail Email Report", dataframe=email_report)
