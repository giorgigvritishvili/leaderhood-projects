
async function getWeather() {
    const city = document.getElementById('cityInput').value;
    const apiKey = '3bd9b53a9b9d4d36894133733241011';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
  
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('City not found');
      
      const data = await response.json();
      displayWeather(data);
    } catch (error) {
      alert('Error fetching weather data. Please check the city name.');
    }
  }
  
  function displayWeather(data) {
    const weatherResult = document.getElementById('weatherResult');
    
    const temperature = data.main.temp;
    const weather = data.weather[0].description;
    const iconCode = data.weather[0].icon;
  
    weatherResult.innerHTML = `
      <h2>${data.name}</h2>
      <img src="http://openweathermap.org/img/wn/${iconCode}@2x.png" alt="${weather}">
      <p class="temp">${temperature}°C</p>
      <p>${weather}</p>
    `;
    weatherResult.style.display = 'block';
  }
  


