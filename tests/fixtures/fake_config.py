from KerbalStuff.config import config, env


# IMPORT THIS FIRST.
# The config module hard-loads config.ini, and other modules import it directly,
# so we need to cheat to override it.
if not config.has_section(env):
    config.add_section(env)
config[env]['connection-string'] = 'sqlite:///:memory:'
config[env]['protocol'] = 'https'
config[env]['domain'] = 'tests.spacedock.info'
config[env]['ksp-game-id'] = '1'
if 'profile-dir' in config[env]:
    del config[env]['profile-dir']

dummy = ''
