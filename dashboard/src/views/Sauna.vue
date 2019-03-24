<template>
    <div>
        <h3 :class="{selected: last_chair_person === 0}">Kevin</h3>
        <h3 :class="{selected: last_chair_person === 1}">Tobias</h3>
        <h3 :class="{selected: last_chair_person === 2}">Næjla</h3>
        <button class="button" @click="changeChairPerson()">Bastet!</button>
    </div>
</template>
<script>
    import {HTTP} from "../assets/js/http-common";

    export default {
        name: 'Sauna',
        data() {
            return {
                last_chair_person: 0
            }
        },
        methods: {
            changeChairPerson: function() {
                HTTP.put('sauna/', {
                    last_chair_person: this.last_chair_person >= 2 ? 0 : this.last_chair_person + 1
                }).then(response => {
                    this.last_chair_person = response.data.last_chair_person
                })
            }
        },
        mounted() {
            HTTP.get('sauna/').then((response) => {
                this.last_chair_person = response.data.last_chair_person
            })
        }
    }
</script>
<style scoped lang="scss">
    .selected {
        color: $accent-color;
    }
</style>