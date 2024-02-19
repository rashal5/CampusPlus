document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.querySelector('.sidebar');
    const openSidebarBtn = document.querySelector('.mobile-nav-toggle.mobile-nav-show');
    const closeSidebarBtn = document.querySelector('.close-sidebar');
  
    openSidebarBtn.addEventListener('click', function () {
      sidebar.style.left = '0';
    });
  
    closeSidebarBtn.addEventListener('click', function () {
      sidebar.style.left = '-300px';
    });
  });
  