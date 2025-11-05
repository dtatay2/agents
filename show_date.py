#!/usr/bin/env python3
"""
Simple script to display today's date.
This is a test implementation for the agent.
"""

from datetime import datetime
import locale

def main():
    """Display today's date."""
    today = datetime.now()
    
    # Display in Spanish
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        print(f"Fecha de hoy: {today.strftime('%d de %B de %Y')}")
    except locale.Error:
        # Fallback if Spanish locale is not available
        months_es = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }
        print(f"Fecha de hoy: {today.day} de {months_es[today.month]} de {today.year}")
    
    # Reset to default and display in English
    try:
        locale.setlocale(locale.LC_TIME, '')
    except locale.Error:
        pass
    print(f"Today's date: {today.strftime('%B %d, %Y')}")

if __name__ == "__main__":
    main()
