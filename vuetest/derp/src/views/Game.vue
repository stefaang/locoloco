<template>
  <div class="block md:flex" id="map">
    <div class="flex md:inline-block bg-gray-200 md:bg-gray-400">
      <label class="hidden md:block rounded-lg md:w-40 md:h-40 px-4 py-2 m-2 bg-gray-100">Picture</label>
      <label class="flex-1 md:block rounded-lg md:w-40 px-4 py-2 m-2">User</label>
      <label class="flex-1 md:block rounded-lg md:w-40 px-4 py-2 m-2">Team</label>
      <label class="flex-1 md:block rounded-lg md:w-40 px-4 py-2 m-2">Score</label>
      <button @click="loadMarkers"
              class="hidden md:block rounded-lg md:w-40 px-4 py-2 m-2">Load markers</button>
    </div>
    <MglMap :accessToken="accessToken"
            :mapStyle="mapStyle"
            :center="mapCenter"
            :zoom="defaultZoom"
            :dragRotate=false
            @load="onMapLoaded">
    <MglNavigationControl :showZoom="true" :showCompass="false" />

    </MglMap>
  </div>
</template>

<script>

import Mapbox from 'mapbox-gl'
import { MglMap, MglNavigationControl } from 'vue-mapbox'
import axios from 'axios'

export default {
  components: {
    MglMap,
    MglNavigationControl
  },
  data () {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_TOKEN,
      defaultZoom: 12,
      mapCenter: [3.735, 51.015],
      mapStyle: 'mapbox://styles/mapbox/streets-v9'
    }
  },
  methods: {
    async onMapLoaded(event) {
    // Actions to run when the map is loaded
      const asyncActions = event.component.actions

      const newParams = await asyncActions.flyTo({
        zoom: 16,
        pitch: 45,
        speed: 1
      })
      console.log(newParams)
    },
    loadMarkers() {
      axios.get('http://localhost:5000/').then(
        function(resp) {
          console.log('Oiii: '+JSON.stringify(resp))
        }
      )
    }
  },
  created () {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox
  },
  mounted () {

  }
}

</script>

<style scoped lang="scss">

  #map {
    padding: 10px;
    height: 30em;
  }

</style>


