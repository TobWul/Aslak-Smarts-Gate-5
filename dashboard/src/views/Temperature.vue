<template>
    <div id="temperature">
        <h1>Temperaturer</h1>
        <div class="card">
            <line-chart :chart-data="datacollection"></line-chart>
        </div>
    </div>
</template>
<script>
    import LineChart from "../components/LineChart";
    import axios from 'axios'
    import {HTTP} from "@/assets/js/http-common";

    export default {
        name: 'temperature',
        components: {LineChart},
        data() {
            return {
                temperatures: [],
                timestamps: [],
                loaded: false,
                datacollection: {
                    labels: this.timestamps,
                    datasets: [
                        {
                            label: 'Temperature',
                            backgroundColor: '#ffffff',
                            data: this.temperatures
                        }
                    ]
                }
            }
        },
        methods: {
            setDatacollection: function() {
                this.datacollection = {
                    labels: this.timestamps,
                        datasets: [
                        {
                            label: 'Temperature',
                            backgroundColor: 'rgba(0,0,0,0)',
                            borderColor: 'rgba(255,255,255,0.6)',
                            data: this.temperatures
                        }
                    ]
                }
            },
          convertTemperatures: function(temperatures) {
              for (let i = 0; i < temperatures.length; i++) {
                  let time = new Date(temperatures[i].timestamp)
                  this.timestamps.push(`${time.getHours()}:${time.getMinutes()}`);
                  this.temperatures.push(temperatures[i].temperature);
                  this.setDatacollection();

              }
              console.log(this.timestamps, this.temperatures)
          }
        },
        mounted() {
            axios
                .get('http://localhost:8000/api/' + 'inside-temperatures')
                .then((response) => (
                    this.convertTemperatures(response.data)
                ))
        }
    }
</script>