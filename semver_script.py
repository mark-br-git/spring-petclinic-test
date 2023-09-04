import semver
import sys

current_version = sys.argv[1]
parsed_version = semver.VersionInfo.parse(current_version)
new_version1 = parsed_version.bump_minor()
new_version2 = new_version1.bump_minor()
new_version = new_version2.bump_minor()

print(new_version)


