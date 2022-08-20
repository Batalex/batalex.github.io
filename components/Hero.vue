<template>
    <div class="relative shadow-xl sm:overflow-hidden">
        <div class="absolute inset-0">
            <canvas id="canvas" class="h-full w-full text-laurel-green"></canvas>
        </div>
        <div class="px-4 py-16 sm:px-6 sm:py-20 lg:py-24 lg:px-32">
            <div
                class="text-left max-w-3xl  mx-auto relative">
                <h1 class="text-4xl w-full text-left text-jet font-bold tracking-tight sm:text-5xl lg:text-6xl">
                    Hi,<br/>I am <span class="font-black">Alex</span>.
                </h1>
                <p class="mt-6 max-w-lg text-xl text-olive-drab sm:max-w-3xl">
                    I am a data scientist & software engineer based in Lyon (FR).
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
onMounted(() => {
    let canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d');
    let w = window.innerWidth;
    let h = window.innerHeight;
    canvas.width = w;
    canvas.height = h;
    ctx.fillStyle = "#635F54"

    let M = 4294967296,
        // a - 1 should be divisible by m's prime factors
        A = 1664525,
        // c and m should be co-prime
        C = 1;
    let Z = Math.floor(Math.random() * M);

    function rand() {
        Z = (A * Z + C) % M;
        return Z / M - 0.5;
    };

    function interpolate(pa, pb, px) {
        let ft = px * Math.PI,
            f = (1 - Math.cos(ft)) * 0.5;
        return pa * (1 - f) + pb * f;
    }

    for (let i = 0; i <= 2; i++) {
        let x = 0,
            y = h / 2,
            amp = 0.3, //amplitude
            wl = 200, //wavelength
            fq = 1 / wl, //frequency
            a = rand(),
            b = rand();

        while (x < w) {
            if (x % wl === 0) {
                a = b;
                b = rand();
                y = h / 2 + a * amp * x;
            } else {
                y = h / 2 + interpolate(a, b, (x % wl) / wl) * (amp*x);
            }
            ctx.fillRect(x, y, 1, 1);
            x += 1;
        }
    }

})

</script>
