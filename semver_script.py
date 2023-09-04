import semver
import sys

current_version = "1.2.0"
parsed_version = semver.VersionInfo.parse(current_version)
new_version = parsed_version.bump_minor()

print(new_version)


