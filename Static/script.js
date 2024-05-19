document.getElementById('weatherForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    document.getElementById('statusMessage').classList.remove('hidden');
    
    const city = document.getElementById('location').value;
    const date = document.getElementById('date').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                city,
                date,
            }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        document.getElementById('cityName').textContent =  city + " Weather ";
        document.getElementById('avgTemp').textContent = data.avg_temp + " °C ";
        document.getElementById('avgPres').textContent = data.avg_pres + " mb ";
        document.getElementById('avgWdir').textContent = "   "+data.avg_wdir ;
        document.getElementById('avgWspd').textContent = data.avg_wspd;

        // Get the day of the week from the selected date
        const selectedDate = new Date(date);
        const options = { weekday: 'long' };
        const dayOfWeek = selectedDate.toLocaleDateString('en-US', options);

        // Create elements for date and day of the week
        const dateElement = document.createElement('p');
        dateElement.textContent = ` ${date} ${dayOfWeek}`;
        dateElement.classList.add('date-info');


        // Append elements to the cityName element
        const cityNameElement = document.getElementById('cityName');
        cityNameElement.appendChild(dateElement);
        cityNameElement.appendChild(dayOfWeekElement);

    } catch (error) {
        console.error('Error:', error);
    }
});
