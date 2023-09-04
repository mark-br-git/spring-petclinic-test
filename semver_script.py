import semver
import subprocess

# Get the current Git tag
try:
    current_tag = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).decode("utf-8").strip()
except subprocess.CalledProcessError:
    current_tag = "0.0.0"  # If no tags are found, start with version 0.0.0

# Parse the current version
parsed_version = semver.VersionInfo.parse(current_tag)

# Increment the minor version for each commit
parsed_version = parsed_version.bump_minor()

# Print the new version
print(parsed_version)
