const items = [
    {
        position: 0,
        el: document.getElementById('carousel-item-1')
    },
    {
        position: 1,
        el: document.getElementById('carousel-item-2')
    },
    {
        position: 2,
        el: document.getElementById('carousel-item-3')
    },
];

const options = {
    activeItemPosition: 1,
    interval: 9000,

    indicators: {
        activeClasses: 'bg-white dark:bg-gray-800',
        inactiveClasses: 'bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800',
        items: [
            {
                position: 0,
                el: document.getElementById('carousel-indicator-1')
            },
            {
                position: 1,
                el: document.getElementById('carousel-indicator-2')
            },
            {
                position: 2,
                el: document.getElementById('carousel-indicator-3')
            },
        ]
    },
};

const carousel = new Carousel(items, options);

carousel.cycle()

const prevButton = document.getElementById('data-carousel-prev');
const nextButton = document.getElementById('data-carousel-next');

prevButton.addEventListener('click', () => {
    carousel.prev();
});

nextButton.addEventListener('click', () => {
    carousel.next();
});