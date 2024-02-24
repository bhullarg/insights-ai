import os

def read_text(filepath):
    """
    Get the contents of a text file
    """
    with open(filepath, 'r') as file:
        return file.read()
    
def get_summary(text):
    """
    return the first two lines
    """
    return "\n".join(text.split("\n")[:2])

def save_summary(savedir, summary):
    """
    Save summary as text file in savedir
    """
    with open(os.path.join(savedir, "summary.txt"), 'w') as file:
        file.write(summary)