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

      <MglMarker
					v-for="marker in payload"
					:coordinates="[marker.lng, marker.lat]"
					:draggable="true"
					:color.sync="marker.color"
					:markerId="marker.id"
					:key="marker.id + '-' + marker.color"
					ref="markers"
			>
        <MglPopup>
          <div class="flex items-center">
            <span
              class="text-xs inline-flex items-center justify-center p-3 mr-2 w-4 h-4 rounded-full"
              :class="{
                'bg-teal-800 text-teal-100': markerColor == 'blue',
                'bg-red-800 text-red-100': markerColor == 'red',
              }"
            >
              {{ marker.id }}
            </span>
            <span class="text-sm">{{ marker.color }}</span>
          </div>
        </MglPopup>
        <!-- @click="markerClicked" -->
      </MglMarker>
    </MglMap>
  </div>
</template>

<script>

import Mapbox from 'mapbox-gl'
import { MglMap, MglNavigationControl, MglMarker, MglPopup } from 'vue-mapbox'
import $backend from '../backend'

export default {
  components: {
    MglMap,
    MglMarker,
    MglNavigationControl,
    MglPopup
  },
  data () {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_TOKEN,
      defaultZoom: 12,
      mapCenter: [3.735, 51.015],
      mapStyle: 'mapbox://styles/mapbox/streets-v11',
      payload: [],
      markerColor: 'blue',
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
      // track position
      setInterval(this.loadMarkers, 3000)
      //
    },

    animateMarkers(timestamp) {
      const duration = 2000
      if (!this.start) this.start = timestamp
      let progress = timestamp - this.start
      // update markers
      this.payload.forEach(
        (marker, index) => {
          if (!marker.anim) return
          marker.lng = (progress/duration)*marker.anim.newLng + (1-progress/duration)*marker.anim.oldLng
          marker.lat = (progress/duration)*marker.anim.newLat + (1-progress/duration)*marker.anim.oldLat
          this.payload.splice(index, 1, marker)
        }
      )
      // schedule next frame
      if (progress < duration) {
        requestAnimationFrame(this.animateMarkers)
      } else {
        this.start = null
        this.payload.forEach(
          marker => {
            marker.anim = null
          }
        )
      }
    },

    async loadMarkers() {
      $backend.fetchMarkers()
        .then(markerData => {
          markerData.forEach(marker => {
            let mIndex = this.payload.findIndex(m => m.id == marker.id)

            if (mIndex > -1) {
              // Update existing marker
              let origMarker = this.payload[mIndex]
              marker.anim = {
                oldLng: origMarker.lng,
                oldLat: origMarker.lat,
                newLng: marker.lng,
                newLat: marker.lat
              }
              marker.lng = marker.anim.oldLng
              marker.lat = marker.anim.oldLat
              this.payload.splice(mIndex, 1, marker)
            } else {
              // Add new marker
              this.payload.push(marker)
            }
          })
          requestAnimationFrame(this.animateMarkers)
        }).catch(error => {
          this.error = error.message
      });

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


