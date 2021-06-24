<template>
    <div>
        <Title titleName="About me"/>

        <figure class="flex mt-8 px-4 items-center sm:flex-col">
            <img alt="Young Alex" class="w-32 h-32 md:w-48 h-auto rounded-full mx-auto"
                 height="512" src="~assets/alex.jpg"
                 width="384">
            <div class="pl-4 text-left md:text-center md:pt-6 space-y-4">
                <figcaption class="font-medium">
                    <div class="text-black text-lg md:text-2xl font-extrabold tracking-normal">
                        Alexandre Batisse
                    </div>
                    <div class="text-normal md:text-xl">
                        <span class="font-bold">Data scientist & Tech lead</span> at HEVA
                    </div>
                </figcaption>
            </div>
        </figure>
        <div class="text-black text-normal md:text-lg py-4 md:py-8 lg:py-8">
            <p>
                My manifold technical interests include software engineering, statistics, and data
                visualization. I try to cultivate a diverse set of skills. Thus, I feel just as
                confident writing a data preprocessing script, serving a model in a web server, or
                setting up a CI pipeline for unit tests.
            </p>

            <p class="mt-2">Technology watch makes a significant part of my typical day, as I like
                to be in touch
                with the latest Python or analytics tools news.
                I feel strongly about the FOSS mindset. I try to contribute to the projects I like
                when I can.
            </p>

            <p class="mt-2">
                I majored with honors (M.Sc.Eng) in telecommunications in 2017.
            </p>
        </div>

        <h2 class="text-2xl text-center text-black font-extrabold tracking-normal sm:text-2xl lg:text-3xl">
            Get in touch</h2>
        <div
            class="flex grid-flow-col justify-between mx-auto max-w-sm md:max-w-md py-4 md:py-8 lg:py-8">
            <a class="text-4xl hover:text-green-500 transition"
               href="mailto:alexandre.batisse@hey.com"
               target="_blank">
                <font-awesome-icon icon="envelope"/>
            </a>
            <a class="text-4xl hover:text-green-500 transition" href="https://github.com/batalex"
               target="_blank">
                <font-awesome-icon :icon="['fab', 'github']"/>
            </a>
            <a class="text-4xl hover:text-green-500 transition" href="https://gitlab.com/abatisse"
               target="_blank">
                <font-awesome-icon :icon="['fab', 'gitlab']"/>
            </a>

        </div>
    </div>
</template>
