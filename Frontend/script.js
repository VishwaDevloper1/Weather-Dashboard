function getWeather() {
    let city = document.getElementById("city").value;
    fetch(`http://localhost:5000/weather/${city}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").innerText = JSON.stringify(data, null, 2);
        });
}
