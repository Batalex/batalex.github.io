<template>
    <div class="bg-white overflow-hidden">
        <Hero/>
        <div class="relative overflow-hidden">
            <div aria-hidden="true"
                 class="hidden sm:block sm:absolute sm:inset-y-0 sm:h-full sm:w-full">
                <div class="relative h-full max-w-7xl mx-auto">
                    <svg
                        class="absolute right-full transform translate-y-1/4 translate-x-1/4 lg:translate-x-1/2"
                        fill="none" height="784" viewBox="0 0 404 784" width="404">
                        <defs>
                            <pattern id="f210dbf6-a58d-4871-961e-36d5016a0f49" height="20"
                                     patternUnits="userSpaceOnUse"
                                     width="20" x="0" y="0">
                                <rect class="text-gray-200" fill="currentColor" height="4" width="4"
                                      x="0"
                                      y="0"/>
                            </pattern>
                        </defs>
                        <rect fill="url(#f210dbf6-a58d-4871-961e-36d5016a0f49)" height="784"
                              width="404"/>
                    </svg>
                    <svg
                        class="absolute left-full transform -translate-y-3/4 -translate-x-1/4 md:-translate-y-1/2 lg:-translate-x-1/2"
                        fill="none" height="784" viewBox="0 0 404 784" width="404">
                        <defs>
                            <pattern id="5d0dd344-b041-4d26-bec4-8d33ea57ec9b" height="20"
                                     patternUnits="userSpaceOnUse"
                                     width="20" x="0" y="0">
                                <rect class="text-gray-200" fill="currentColor" height="4" width="4"
                                      x="0"
                                      y="0"/>
                            </pattern>
                        </defs>
                        <rect fill="url(#5d0dd344-b041-4d26-bec4-8d33ea57ec9b)" height="784"
                              width="404"/>
                    </svg>
                </div>
            </div>
            <div class="max-w-7xl mx-auto relative px-4 py-16 sm:px-6 sm:pt-24 lg:pt-32 lg:px-32">
                <About/>
                <Experiences/>
                <Projects/>
            </div>

        </div>
        <footer class="bg-white">
            <div
                class="text-left max-w-7xl mx-auto relative px-4 pt-8 pb-2 sm:px-6 sm:pt-12 lg:pt-16 lg:px-32">

                <p class=" text-base text-gray-400">
                    Photo by <a class="text-green-500 external hover:underline"
                                href="https://unsplash.com/@stayhome"
                                target="_blank">Alena Stepanova</a>.
                </p>
            </div>
        </footer>
    </div>

</template>

<style>
.external::after {
    content: "\00A0[↪]";
}
</style>
