#!/usr/bin/env python3
"""
Simple script to display today's date.
This is a test implementation for the agent.
"""

from datetime import datetime

def main():
    """Display today's date."""
    today = datetime.now()
    print(f"Fecha de hoy: {today.strftime('%d de %B de %Y')}")
    print(f"Today's date: {today.strftime('%B %d, %Y')}")

if __name__ == "__main__":
    main()
