from config_data.config import load_config

config = load_config('.env')

token = config.tg_bot.token
superadmin = config.tg_bot.admin_ids[0]

print(f"BOT_TOKEN: {token}")
print(f"ADMIN_IDS: {config.tg_bot.admin_ids}")
print(f"SUPER ADMIN: {superadmin}")
print()
print(f"DATABASE: {config.db.database}")
print(f"DB_HOST: {config.db.db_host}")
print(f"DB_USER: {config.db.db_user}")
print(f"DB_PASSWORD: {config.db.db_password}")