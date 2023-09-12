---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I'm Yi Bao, a researcher in the realm of geospatial sciences. I've pursued and obtained my Ph.D. in Cartography and Geographic Information Systems from Peking University and previously completed my Bachelor's in Information Engineering at China University of Geosciences, Wuhan.

Central to all my research endeavors is my commitment to sustainable urban development. I firmly believe in the transformative power of machine learning and spatial analysis techniques to craft a more sustainable and environmentally-conscious urban future. I'm always excited to collaborate and discuss my work, so please feel free to reach out. Let's pave the way for a more sustainable urban future together!

## **Education:**
- **Ph.D., Cartography and Geographic Information Systems**, Peking University, Sept 2018 - Jul 2023. Advisor: Prof. Zhou Huang.
- **B.S., Information Engineering**, China University of Geosciences, Wuhan, Sept 2014 - Jul 2018.

## **Honors and Awards:**
- Outstanding Ph.D. Dissertation Award, Peking University, 2023.
- Excellent Graduate, Peking University, 2023.
-Outstanding Research Award, Peking University, 2020, 2022.
- Outstanding Academic Paper Award, Remote Sensing Institute, Peking University, 2020, 2022.
- Leo KoGuan Scholarship, Peking University, 2020.
- Excellent Graduate, China University of Geosciences, Wuhan, 2018.
- National Scholarship, 2015, 2016.
- Li Siguang Program, 9th Edition, China University of Geosciences, Wuhan, 2015.

## **Research Interests:**
- **Urban Spatio-temporal Big Data Mining:** Using data analytics to reveal urban development patterns and trends, aiding urban planning and policy-making.

- **High-resolution Studies on Urban Built Environment Material Stocks:** Using machine learning and geo big data to compute urban stocks for sustainable development and urban evolution direction.

- **Exploring the Interactions between Built Environment and Human Activities:** Analyzing the influence and interplay between urban environments, human activities, and socio-economic attributes.

## **Publications:**

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}