function fireworks() {
    var duration = 5 * 1000;
    var animationEnd = Date.now() + duration;
    var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

    function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    var interval = setInterval(function() {
        var timeLeft = animationEnd - Date.now();

        if (timeLeft <= 0) {
            return clearInterval(interval);
        }

        var particleCount = 50 * (timeLeft / duration);
        confetti({ ...defaults, particleCount, origin: { x: randomInRange(0, 1), y: Math.random() - 0.2 } });
    }, 250);
}

function stars() {
    var defaults = {
        spread: 360,
        ticks: 50,
        gravity: 0,
        decay: 0.94,
        startVelocity: 30,
        colors: ['FFE400', 'FFBD00', 'E89400', 'FFCA6C', 'FDFFB8']
    };

    function shoot() {
        confetti({
            ...defaults,
            particleCount: 40,
            scalar: 1.2,
            shapes: ['star'],
            origin: { x: Math.random(), y: Math.random() - 0.2 }
        });

        confetti({
            ...defaults,
            particleCount: 10,
            scalar: 0.75,
            shapes: ['circle'],
            origin: { x: Math.random(), y: Math.random() - 0.2 }
        });
    }

    setTimeout(shoot, 0);
    setTimeout(shoot, 100);
    setTimeout(shoot, 200);
}

function fire() {
    var end = Date.now() + (2000);
    var colors = ['#bb0000', '#ffffff'];

    (function frame() {
        confetti({
            particleCount: 2,
            angle: 60,
            spread: 55,
            origin: { x: Math.random(), y: Math.random() - 0.2 },
            colors: colors
        });
        confetti({
            particleCount: 2,
            angle: 120,
            spread: 55,
            origin: { x: Math.random(), y: Math.random() - 0.2 },
            colors: colors
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());
}

function emoji() {
    var scalar = 2;
    var unicorn = confetti.shapeFromText({ text: '🎉', scalar });

    var defaults = {
        spread: 360,
        ticks: 60,
        gravity: 0,
        decay: 0.96,
        startVelocity: 20,
        shapes: [unicorn],
        scalar,
        origin: { x: Math.random(), y: Math.random() - 0.2 }
    };

    function shoot() {
        confetti({
            ...defaults,
            particleCount: 30
        });

        confetti({
            ...defaults,
            particleCount: 5,
            flat: true
        });

        confetti({
            ...defaults,
            particleCount: 15,
            scalar: scalar / 2,
            shapes: ['circle']
        });
    }

    setTimeout(shoot, 0);
    setTimeout(shoot, 100);
    setTimeout(shoot, 200);
}

let lastIndex = -1;
document.getElementById('btnConfetti').addEventListener('click', function() {
    const functions = [fireworks, stars, fire, emoji];
    let randomIndex = lastIndex;

    while (randomIndex === lastIndex) {
        randomIndex = Math.floor(Math.random() * functions.length);
    }

    lastIndex = randomIndex;
    functions[randomIndex]();
}); 