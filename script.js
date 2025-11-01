function downloadZip() {
    const filesToZip = [
        '_routelog.bat',
        'routings.py',
        'functions.py',
        'routenumcheck.cs',
        'RouteProcessor.dll',
        'LICENSE',
        'README.md',
        'references/aircref.json',
        'references/airlref.json',
        'references/airpcoords.json',
        'references/cityref.json',
        'references/country_names.json',
        'references/countryref.json',
        'references/firref.json',
        'references/iatacodes.json',
        'references/navaids.json'
    ];

    alert('Download functionality would typically package these files:\n\n' +
          filesToZip.join('\n') +
          '\n\nPlease visit the GitHub repository to download the full project.');

    window.open('https://github.com/PineappleCrazy/Routelog', '_blank');
}

document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });

    const cards = document.querySelectorAll('.feature-card, .tool-card, .step');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s, transform 0.6s';
        observer.observe(card);
    });
});