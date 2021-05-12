from distutils.util import strtobool
import os

# Use clear console after each command
USE_CLEAR_AFTER_CMD = strtobool(os.getenv("GTFF_USE_CLEAR_AFTER_CMD", "True"))

# Use coloring features
USE_COLOR = strtobool(os.getenv("GTFF_USE_COLOR", "True"))

# Select console flair (choose from config_terminal.py list)
USE_FLAIR = os.getenv("GTFF_USE_FLAIR") or "stars"

# Enable interactive matplotlib mode
USE_ION = strtobool(os.getenv("GTFF_USE_ION", "True"))

# Enable Prompt Toolkit
USE_PROMPT_TOOLKIT = strtobool(os.getenv("GTFF_USE_PROMPT_TOOLKIT", "True"))

# Enable Prediction features
ENABLE_PREDICT = strtobool(os.getenv("GTFF_ENABLE_PREDICT", "True"))

# Enable FB Prophet
ENABLE_FBPROPHET = strtobool(os.getenv("GTFF_ENABLE_FBPROPHET", "True"))

# Enable plot autoscaling
USE_PLOT_AUTOSCALING = strtobool(os.getenv("GTFF_USE_PLOT_AUTOSCALING", "True"))

# Enable thoughts of the day
ENABLE_THOUGHTS_DAY = strtobool(os.getenv("GTFF_ENABLE_THOUGHTS_DAY", "True"))

# Quick exit for testing
ENABLE_QUICK_EXIT = strtobool(os.getenv("GTFF_ENABLE_QUICK_EXIT", "True"))
