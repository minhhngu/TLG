#!/usr/bin/env python3

# imports always go at the top of your code
import requests

API = "https://api.magicthegathering.io/v1/"  # this will never change regardless of the lookup we perform

supert = input("Input supertype: ").lower()

# f string searches supertypes
resp = requests.get(f"{API}cards?supertypes={supert}")

cards = resp.json()

print(cards)







