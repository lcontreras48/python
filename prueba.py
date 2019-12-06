#!/usr/bin/env python3

"""

    Script para obtener el trm reciente

    by Dorance <dorancemc@gmail.com>

"""

import json
import requests

# functions
def main(command_line=None):
    print(get_trm())


def get_trm():
    headers = { 'Accept': 'application/json' }
    response = requests.get('https://www.datos.gov.co/resource/32sa-8pi3.json', headers=headers)
    data = response.text
    datos = json.loads(data)
    return { datos[0]['vigenciadesde'] : float(datos[0]['valor']) }


# main
if __name__ == '__main__':
    main()
