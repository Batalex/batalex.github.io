<template>
    <div class="bg-white overflow-hidden">
        <Hero />
        <div
            class="text-left max-w-7xl mx-auto relative px-4 pt-16 sm:px-6 sm:pt-24 lg:pt-32 lg:px-32 ">
            <div class="hidden lg:block lg:absolute lg:inset-0 lg:h-full lg:w-full mix-blend-multiply z-0">
                <div class="relative h-full text-lg max-w-prose mx-auto" aria-hidden="true">
                    <svg class="absolute top-12 left-full transform translate-x-32" width="404"
                         height="384" fill="none" viewBox="0 0 404 384">
                        <defs>
                            <pattern id="74b3fd99-0a6f-4271-bef2-e80eeafdf357" x="0" y="0"
                                     width="25"
                                     height="25" patternUnits="userSpaceOnUse">
                                <rect x="0" y="0" width="5" height="5" class="text-indigo-100"
                                      fill="currentColor"/>
                            </pattern>
                        </defs>
                        <rect width="404" height="384"
                              fill="url(#74b3fd99-0a6f-4271-bef2-e80eeafdf357)"/>
                    </svg>
                    <svg
                        class="absolute top-1/2 right-full transform -translate-y-1/2 -translate-x-32"
                        width="404" height="384" fill="none" viewBox="0 0 404 384">
                        <defs>
                            <pattern id="f210dbf6-a58d-4871-961e-36d5016a0f49" x="0" y="0"
                                     width="25"
                                     height="25" patternUnits="userSpaceOnUse">
                                <rect x="0" y="0" width="5" height="5" class="text-indigo-100"
                                      fill="currentColor"/>
                            </pattern>
                        </defs>
                        <rect width="404" height="384"
                              fill="url(#f210dbf6-a58d-4871-961e-36d5016a0f49)"/>
                    </svg>
                    <svg class="absolute bottom-12 left-full transform translate-x-32" width="404"
                         height="384" fill="none" viewBox="0 0 404 384">
                        <defs>
                            <pattern id="d3eb07ae-5182-43e6-857d-35c643af9034" x="0" y="0"
                                     width="25"
                                     height="25" patternUnits="userSpaceOnUse">
                                <rect x="0" y="0" width="5" height="5" class="text-indigo-100"
                                      fill="currentColor"/>
                            </pattern>
                        </defs>
                        <rect width="404" height="384"
                              fill="url(#d3eb07ae-5182-43e6-857d-35c643af9034)"/>
                    </svg>
                </div>
            </div>
            <div class="relative z-10">
                <About />
<!--                <Experiences />-->
                <Projects />
            </div>

        </div>
        <footer class="bg-white">
            <div
                class="text-left max-w-7xl mx-auto relative px-4 pt-8 pb-2 sm:px-6 sm:pt-12 lg:pt-16 lg:px-32">

                <p class=" text-base text-gray-400">
                    Photo by <a class="text-green-400 external hover:text-green-600"
                                href="https://unsplash.com/@stayhome"
                                target="_blank">Alena Stepanova</a>.
                </p>
            </div>
        </footer>
    </div>


</template>

<script>
export default {}
</script>

<style>
.external::after {
    content: "\00A0[↪]";
}
</style>
