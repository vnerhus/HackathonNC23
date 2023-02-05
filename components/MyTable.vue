<template>
  <div class="table__container">
    <div class="table__header">
      <span class="table__title">LUNSJMENY</span>
      <div class="title_divider"></div>
      <span class="table__week">Uke 6: Mandag</span>
    </div>
    <el-table class="table__s" :data="tableData" style="width: 100%">
      <el-table-column class="colum" prop="date" label="Type" width="180" />
      <el-table-column prop="name" label="Lunsjbeskrivelse" />
    </el-table>
  </div>
</template>
  
<script lang="ts" setup>
  const tableData = [
    {
      date: 'Lunsj',
      name: 'Kylling korma med raita,  mangochutney og nan basmatiris',
      allergen:'(melk, hvete,  cashewnøt, hvitløk)'
    },
    {
      date: 'Lunsj veg',
      name: 'Palak paneer m rita mangochutny basmatiris nan',
      allergen: '(melk, hvete,  sulfit)'
    },
    {
      date: 'Dagens påsmurt',
      name: 'Langpanne rotspelt,  med serrano,  syltarødløk,  brie og aioli.',
      allergen: '(hvete,  egg,  sennep,  sulfitt,  hvitløk,  melk)'
    },
    {
      date: 'Dagens påsmurt veg',
      name: 'Langpanne rotspelt,  med tomat,  syltarødløk,  brie og aioli.',
      allergen: '(hvete,  egg,  sennep,  sulfitt,  hvitløk,  melk)'
    },
    {
      date: 'Dagens salat',
      name: 'Bulgursalat marinert bulgur med og grønnsaksmix,  med grillet svinenakke. Syltet rødløk.',
      allergen: '(hvete,  sulfitt)'
    },
    {
      date: 'Dagens salat veg',
      name: 'Bulgursalat,  marinert bulgur og grønnsaksmix,  med feta ,  oliven og Syltet rødløk.',
      allergen: '(hvete,  melk,  sulfitt)'
    },
  ]
</script>
<style>

  .table__header {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .table__title {
    font-size: 50px;
  }

  .title_divider {
    background-color: white;
    width: 2px;
    height: 40px;
    margin-bottom: 6px;
  }

  .table__week {
    font-size: 30px;
    font-family: GeomanistRegular;
  }

  .table__container {
    padding: 40px;
    color: white;
    background-color: #141448;
    margin-left: 20px;
    margin-right: 20px;
    border-radius: 10px;
  }

  .table__s {
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 10px;
  }

  .colum {
    padding: 10px;
  }

  .el-table__cell {
    padding: 15px !important;
    font-family: GeomanistRegular;
    font-size: 15px;
  }

</style>