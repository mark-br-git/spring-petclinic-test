import semver
import sys

current_version = sys.argv[1]
parsed_version = semver.VersionInfo.parse(current_version)
new_version = parsed_version.bump_minor()

print(new_version)


