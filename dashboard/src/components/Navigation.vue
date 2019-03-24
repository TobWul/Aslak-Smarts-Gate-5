<template>
    <nav>
        <router-link to="/"><img src="@/assets/icons/Home.svg" alt="Home">Oversikt</router-link>
        <router-link to="/electricity"><img src="@/assets/icons/Electricity.svg" alt="Electricity">Straum</router-link>
        <router-link to="/sauna"><img src="@/assets/icons/Electricity.svg" alt="Sauna">Badstuo</router-link>
        <router-link to="/temperature"><img src="@/assets/icons/Analytics.svg" alt="Temperatur">Temperatur</router-link>
        <router-link to="/settings"><img src="@/assets/icons/Settings.svg" alt="Settings">Innstillinger</router-link>
    </nav>
</template>

<script>
    export default {
        name: 'Navigation',
        props: {
            msg: String
        }
    }
</script>

<style scoped lang="scss">
    nav {
        position: fixed;
        left: 0;
        top: 0;
        height: 100vh;
        width: $nav-width;
        padding-top: 6rem;

        a {
            position: relative;
            color: $light-gray;
            text-decoration: none;
            display: block;
            padding: 1rem 1rem 1rem calc(24px + 2rem);
            border-radius: 0 8px 8px 0;

            &.router-link-exact-active {
                background-color: #131A27;
                font-weight: bold;
                color: $accent-color;

                &::after {
                    content: '';
                    height: 100%;
                    width: 4px;
                    position: absolute;
                    left: 0;
                    top: 0;
                    background-color: $accent-color;
                }
            }

            img {
                position: absolute;
                top: 50%;
                left: 1rem;
                transform: translateY(-50%);
            }
        }
    }
</style>
