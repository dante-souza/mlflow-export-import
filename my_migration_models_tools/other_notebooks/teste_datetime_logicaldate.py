# Databricks notebook source
from datetime import datetime
from zoneinfo import ZoneInfo
print(f"datetime.now no cluster: {datetime.now(ZoneInfo('America/Sao_Paulo'))}")
