# Pruebas de Rendimiento de SauceDemo

Este proyecto documenta las pruebas de rendimiento realizadas en el sitio web de [SauceDemo](https://www.saucedemo.com/). Dado que SauceDemo no proporciona una API oficial, se llevaron a cabo pruebas de rendimiento simulando múltiples usuarios accediendo al sitio a través de Postman y Lighthouse.

## Metodología

### Pruebas en Postman

Se realizaron pruebas de carga utilizando Postman, simulando el acceso simultáneo de múltiples usuarios a la interfaz de usuario de SauceDemo. Esto permitió evaluar el rendimiento del sitio web bajo condiciones de uso intensivo.

- **Duración de las pruebas:** Se ejecutaron dos reportes de 10 minutos cada uno.
- **Resultados:** Los reportes mostraron resultados casi idénticos en cuanto a la respuesta del servidor y el tiempo de carga, lo que sugiere que el rendimiento del sitio se mantuvo consistente durante las pruebas.

### Pruebas de Rendimiento con Lighthouse

Además de las pruebas en Postman, se utilizó [Lighthouse](https://developers.google.com/web/tools/lighthouse) para analizar el rendimiento del sitio tanto en escritorio como en dispositivos móviles. Lighthouse proporciona métricas clave que ayudan a entender la velocidad de carga y la experiencia del usuario.

## Resultados

Las pruebas realizadas en Postman y Lighthouse proporcionaron información valiosa sobre el rendimiento de SauceDemo, teniendo en cuenta que no se cuenta con una API específica para realizar pruebas más profundas. Los resultados obtenidos muestran que:

- La velocidad de respuesta del servidor es adecuada para una experiencia de usuario fluida.
- El sitio mantiene un rendimiento consistente bajo carga moderada de usuarios.

## Conclusiones

A pesar de las limitaciones debido a la ausencia de una API, se llevaron a cabo las pruebas de rendimiento en SauceDemo utilizando herramientas disponibles como Postman y Lighthouse. Estas pruebas han permitido obtener una visión general del rendimiento del sitio, aunque se podrían realizar pruebas adicionales en otros entornos o con diferentes configuraciones para obtener más datos.