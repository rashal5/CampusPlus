function addNewsHeadline() {
    const ticker = document.querySelector('.ticker');
    const newHeadline = document.createElement('span');
    newHeadline.textContent = 'This is a dynamically added news headline. ';
    ticker.appendChild(newHeadline);
}
