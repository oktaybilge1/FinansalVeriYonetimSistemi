package com.test.test;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Altin {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String altin;
    private String son_deger;
    private String alis_deger;
    private String satis_deger;
    private String fark;
    private String tarih;

    // Getter ve Setter metotları
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getAltin() {
        return altin;
    }

    public void setAltin(String altin) {
        this.altin = altin;
    }

    public String getSon_deger() {
        return son_deger;
    }

    public void setSon_deger(String son_deger) {
        this.son_deger = son_deger;
    }

    public String getAlis_deger() {
        return alis_deger;
    }

    public void setAlis_deger(String alis_deger) {
        this.alis_deger = alis_deger;
    }

    public String getSatis_deger() {
        return satis_deger;
    }

    public void setSatis_deger(String satis_deger) {
        this.satis_deger = satis_deger;
    }

    public String getFark() {
        return fark;
    }

    public void setFark(String fark) {
        this.fark = fark;
    }

    public String getTarih() {
        return tarih;
    }

    public void setTarih(String tarih) {
        this.tarih = tarih;
    }
}
