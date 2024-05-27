<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="http://openweathermap.org/img/wn/09d@2x.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PPY Weather App</h3>

  <p align="center">
    An awesome Weather Application written in KivyMD
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

![][product-screenshot]

A weather app that allows users to search for locations, retrieve weather forecasts, and display the forecast graphically on an interactive slider. The app is cross-platform, developed using the Kivy framework and the Kivy MD library.
Technology

* Framework: Kivy
* UI Library: Kivy MD
* Weather Forecast API: Open Meteo
* Geocode API: Open Street Map
* Target Platforms: Android, iOS

# Features

* Location Search
    Enter the name of a city and retrieve its geographical coordinates (X, Y) using an API.

* Weather Forecast Retrieval
    Fetch weather forecast data (temperature, wind, rain) using the Open Meteo API.

* Weather Forecast Display
    Display the forecast with day-to-day accuracy on an interactive slider.
    Show two parameters: pictorial weather and temperature.

Installation
Requirements

* `Python 3.7 or higher`
* `Kivy`
* `Kivy MD`

Installation Steps

1. Clone the repository
```
git clone https://github.com/s20912pjwstkedupl/PPY-Weather-App.git
cd PPY-Weather-App
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the application
```    
python main.py
```

Usage
1. Open the app on your device.
2. Enter the name of a city in the search field.
3. Press the search button.
4. Browse the weather foreocast using the interactive slider.

Directory Structure

bash
```
src/
│
├── main.py             # Main application file
├── load_kv.py          # Kivy .kv files injector
├── weatherapp.kv       # Common kivy screen mapping
├── buildozer.spec      # Buildozer cross-platform config
├── requirements.txt    # List of dependencies
├── dist/               # Graphic resources
│   └── static/         # Weather static icons mappings
└── api/                # External API implementation
├── kv/                 # .kv files with UI definitions
└── Screens/            # Application screens files
└── Components/         # Application reusable molecules
```

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

### Thank you for using our weather app! We hope it will be useful for you.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
