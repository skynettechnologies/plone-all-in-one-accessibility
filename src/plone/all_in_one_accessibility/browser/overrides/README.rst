This directory must exist in the installed package, even when empty.

browser/configure.zcml registers it with z3c.jbot:

    <browser:jbot directory="overrides" layer="...IPloneAllInOneAccessibilityLayer" />

z3c.jbot's ZCML handler calls os.listdir() on this path unconditionally
when Zope loads ZCML at startup. If the directory is missing, Zope fails
to start entirely (ConfigurationExecutionError / FileNotFoundError) --
this is not caught or made optional.

Empty directories are not preserved by sdist/wheel packaging (tar, zip,
and setuptools' MANIFEST-driven file list all only ever capture actual
files, never empty directories). So this placeholder file must stay
here for as long as browser/overrides/ has no real override templates
in it -- do not remove it as "unused"/"cleanup", or the package will
fail to start on a clean install.

Drop template-override .pt files directly in this directory once you
have any; at that point this README can be removed, since the
directory will no longer be empty.
