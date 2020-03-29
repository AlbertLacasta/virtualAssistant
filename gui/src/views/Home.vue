<template>
    <v-card tile @click="goToMenu">
        <v-img
                class="white--text align-end"
                :src="images.background"
        >
            <v-card-title class="display-3 ml-3">{{timestamp}}</v-card-title>
            <v-card-text class="mt-0 ml-3">
                <v-row align="center" class="pt-0 mt-0">
                    <v-col class="display-1 pt-0 mt-0" cols="6" >
                        23&deg;C
                    </v-col>
                </v-row>
            </v-card-text>
        </v-img>
    </v-card>
</template>

<script>

    export default {
        name: 'Home',
        components: {
        },
        data() {
            return {
                images: {
                    background: require('@/images/gradient.jpg')
                },
                timestamp: ""
            }
        },

        created() {
            setInterval(this.getNow, 1000);
        },
        methods: {
            getNow() {
                const today = new Date();
                const time = today.getHours() + ":" + today.getMinutes();
                this.timestamp = time;
            },

            goToMenu() {
                this.$router.push('Menu')
            }
        }
    }

</script>
