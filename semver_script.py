import semver

# Read the current version from a file or any source you prefer
# For example, you could have a file named version.txt with the current version
with open('version.txt', 'r') as version_file:
    current_version = version_file.read().strip()

# Parse the current version using the semver library
parsed_version = semver.VersionInfo.parse(current_version)

# Increment the minor version for each commit (you can customize this logic)
next_version = f"{parsed_version.major}.{parsed_version.minor + 1}.0"

# Print the next version
print(next_version)
