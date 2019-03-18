<template>
    <div class="home">
        <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
        <div class="components">
            <div class="card clickable"
                 v-for="(component, index) of components"
                 @click="toggleComponent(component.id, index, !component.state)"
                 :class="{on: component.state}">
                {{ component.name }}
            </div>
        </div>
        <div v-if="chart" class="chart">
            <canvas id="canvas">{{ chart }}</canvas>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { HTTP } from "../assets/js/http-common";

    export default {
        name: 'overview',
        data() {
            return {
                components: null,
                // Chart
                chart: null
                // End chart
            }
        },
        methods: {
          toggleComponent: function(id, index, state) {
              HTTP.put('components/' + id, {
                state: state
              }).then((response) => (
                  this.components[index].state = response.data.state
              ));
          }
        },
        mounted() {
            HTTP.get('components')
                .then(response => (
                    this.components = response.data
                ))
        }
    }
</script>
<style scoped lang="scss">
    .components {
        display: grid;
        grid-gap: 1rem;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

        .card {
            @include no-select;
            position: relative;
            cursor: pointer;
            padding-left: calc(24px + 2rem);
            &::before {
                content: '';
                position: absolute;
                left: 1rem;
                top: 50%;
                transform: translateY(-50%);
                border-radius: 100px;
                width: 24px;
                height: 24px;
                box-shadow: inset 1px 1px 4px rgba(21, 33, 56, 0.533345);
            }
            &.on::before {
                background-color: $success;
            }
            &:not(.on)::before {
                background-color: $error;
            }
        }
    }
</style>
