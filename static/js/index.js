document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', () => {
        const currentType = parseInt(cell.dataset.type);
        const newType = (currentType + 1) % 4;
        cell.dataset.type = newType;
        cell.className = 'cell';
        if (newType == 0) cell.classList.add('path');
        if (newType == 1) cell.classList.add('wall');
        if (newType == 2) cell.classList.add('entrance');
        if (newType == 3) cell.classList.add('exit');
    });
});

document.getElementById('sendMap').addEventListener('click', function() {
    const cells = document.querySelectorAll('.cell');
    const map = Array.from(cells).map(cell => {
        if (cell.classList.contains('path')) return 0;
        if (cell.classList.contains('wall')) return 1;
        if (cell.classList.contains('entrance')) return 2;
        if (cell.classList.contains('exit')) return 3;
        return 0; // Default to path if no class matches
    });

    const gridSize = 10;
    const formattedMap = [];
    while(map.length) formattedMap.push(map.splice(0, gridSize));

    fetch('/send-map', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({map: formattedMap}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});