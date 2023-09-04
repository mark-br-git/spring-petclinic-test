import semver
import subprocess

# Function to get the latest Git tag
def get_latest_git_tag():
    try:
        git_tag = subprocess.check_output(['git', 'describe', '--abbrev=0', '--tags'], universal_newlines=True).strip()
        return git_tag
    except subprocess.CalledProcessError:
        return None

# Read the latest Git tag as the current version
current_version = get_latest_git_tag()

if current_version is None:
    print("No Git tags found. Unable to determine current version.")
else:
    # Parse the current version using the semver library
    parsed_version = semver.VersionInfo.parse(current_version)

    # Increment the minor version by 1
    new_version = parsed_version.bump_minor()

    # Print the new version
    print(f"Current Version: {current_version}")
    print(f"New Version: {new_version}")
