<template>
    <div class="electricity">
        <h1>Strøm</h1>
        <div class="card">
            <div v-for="el of electricity">
                <p>{{ el.month }}.{{el.year}}</p>
                <p>{{ el.electricity_cost }}</p>
                <p>{{ el.grid_cost }}</p>
                <p>{{ el.sum }}</p>
                <br>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import { HTTP } from "../assets/js/http-common";

    export default {
        name: "Electricity",
        data() {
            return {
                electricity: null
            }
        },
        mounted() {
            HTTP.get('electricity')
                .then(response => (
                    this.electricity = response.data
                ))
        }
    }
</script>
