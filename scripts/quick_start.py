import os

os.system('yarn create strapi-app backend --quickstart --no-run')
os.system('cd ./backend')
os.system('yarn strapi install graphql')